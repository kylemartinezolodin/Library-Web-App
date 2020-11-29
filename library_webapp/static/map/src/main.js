import * as THREE from '../vendor/three.js/build/three.module.js';

import { OrbitControls } from '../vendor/three.js/examples/jsm/controls/OrbitControls.js';
// import { OrbitControls } from '../../';
import { FlyControls } from '../vendor/three.js/examples/jsm/controls/FlyControls.js';
import { GLTFLoader } from '../vendor/three.js/examples/jsm/loaders/GLTFLoader.js';
import { RGBELoader } from '../vendor/three.js/examples/jsm/loaders/RGBELoader.js';
import { RoughnessMipmapper } from '../vendor/three.js/examples/jsm/utils/RoughnessMipmapper.js';


let camera, controls, scene, renderer;

let viewport_container, feature_container;
let button1, button2, button3

let widthOffset = 10;

button1 = document.querySelector("#but1");
button2 = document.querySelector("#but2");
button3 = document.querySelector("#but3");


init();
render();

function init() {

    // const viewport_container = document.createElement( 'div' );
    // document.body.appendChild( viewport_container );

    // document.querySelector("#main").appendChild( viewport_container );

    viewport_container = document.querySelector("#map-viewport_container");
    feature_container = document.querySelector("#map_container");

    camera = new THREE.PerspectiveCamera( 45, (viewport_container.offsetWidth - widthOffset) / viewport_container.offsetHeight, 0.25, 20 );
    camera.position.set( - 1.8, 0.6, 2.7 );

    scene = new THREE.Scene();

    new RGBELoader()
        .setDataType( THREE.UnsignedByteType )
        .setPath( '../../static/map/assets/environment/equirectangular/' ) // IT'S RELATIVE TO THE INDEX.HTML LOCATION
        .load( 'royal_esplanade_1k.hdr', function ( texture ) {

            const envMap = pmremGenerator.fromEquirectangular( texture ).texture;

            scene.background = envMap;
            scene.environment = envMap;

            texture.dispose();
            pmremGenerator.dispose();

            render();

            // model

            // use of RoughnessMipmapper is optional
            const roughnessMipmapper = new RoughnessMipmapper( renderer );

            const loader = new GLTFLoader().setPath( '../../static/map/assets/models/gltf/test_model/' ); // IT'S RELATIVE TO THE INDEX.HTML LOCATION
            loader.load( 'test_model.glb', function ( gltf ) {

                gltf.scene.traverse( function ( child ) {

                    if ( child.isMesh ) {

                        // TOFIX RoughnessMipmapper seems to be broken with WebGL 2.0
                        // roughnessMipmapper.generateMipmaps( child.material );

                    }

                } );

                scene.add( gltf.scene );

                roughnessMipmapper.dispose();

                render();

            } );

        } );

    console.log("viewport_container-dimensions testing 1 width: " +viewport_container.offsetWidth +" height: " +viewport_container.offsetHeight);

    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( (viewport_container.offsetWidth - widthOffset) / viewport_container.offsetHeight );
    renderer.setSize( viewport_container.offsetWidth - widthOffset , viewport_container.offsetHeight );
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1;
    renderer.outputEncoding = THREE.sRGBEncoding;
    viewport_container.appendChild( renderer.domElement );

    const pmremGenerator = new THREE.PMREMGenerator( renderer );
    pmremGenerator.compileEquirectangularShader();

    const controls = new OrbitControls( camera, renderer.domElement );
    controls.addEventListener( 'change', render ); // use if there is no animation loop
    controls.minDistance = 2;
    controls.maxDistance = 10;
    controls.target.set( 0, 0, - 0.2 );
    controls.update();

    
    // controls = new FlyControls( camera, renderer.domElement );
    // controls.movementSpeed = 1000;
    // controls.domElement = renderer.domElement;
    // controls.rollSpeed = Math.PI / 24;
    // controls.autoForward = false;
    // controls.dragToLook = false;
    // controls.update(1);

    window.addEventListener( 'resize', onResize, false );

    // feature_container = document.querySelector("#map_container");
    // feature_container.addEventListener( 'resize', onResize, false );
    
    // button1.addEventListener( 'click',moveCamera( -2.5121, 3.8016, 6.7234)); // THIS WILL NOT WORK SINCE YOU CANNOT PASS ARGUEMENTS DIRECTLY
    button1.addEventListener( 'click', function() {
        moveCamera( -4.5315, 1.5105, 7.1008);

        document.querySelector("#description_container").innerHTML = document.querySelector("#area-1_description").innerHTML
    });
    
    button2.addEventListener( 'click', function() {
        moveCamera( 1.1862, 1.3003, 8.3347);

        document.querySelector("#description_container").innerHTML = document.querySelector("#area-2_description").innerHTML
    });

    button3.addEventListener( 'click', function() {
        moveCamera( -2.6583, 1.6893, 9.7506);
        
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-3_description").innerHTML
    });

    console.log("viewport_container-dimensions testing 2 width: " +viewport_container.offsetWidth +" height: " +viewport_container.offsetHeight);

}

function onResize() {

    // camera.aspect = window.innerWidth / window.innerHeight;
    camera.aspect = (viewport_container.offsetWidth - widthOffset) / viewport_container.offsetHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( viewport_container.offsetWidth - widthOffset, viewport_container.offsetHeight );

    render();

}

//

function render() {

    renderer.render( scene, camera );
    // controls.update(1);

    // document.querySelector("#x").value="x: " +camera.position.x;
    // document.querySelector("#y").value="y: " +camera.position.y;
    // document.querySelector("#z").value="z: " +camera.position.z;
}

function moveCamera(x, y, z){
    camera.position.set( x, y, z);

    console.log("moved @" +x +", " +y +", " +z);

    render();
}
