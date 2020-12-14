import * as THREE from '../vendor/three.js/build/three.module.js';

import { OrbitControls } from '../vendor/three.js/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from '../vendor/three.js/examples/jsm/loaders/GLTFLoader.js';
import { RGBELoader } from '../vendor/three.js/examples/jsm/loaders/RGBELoader.js';
import { RoughnessMipmapper } from '../vendor/three.js/examples/jsm/utils/RoughnessMipmapper.js';


let camera, controls, scene, renderer;

let viewport_container, feature_container;
let button1, button2, button3, button4, button5;

let widthOffset = 0; // SCROLL OVERFLOW PRUPOSE

var gltfRef; // NOT WORKING, FIX LATER

button1 = document.querySelector("#but1");
button2 = document.querySelector("#but2");
button3 = document.querySelector("#but3");
button4 = document.querySelector("#but4");
button5 = document.querySelector("#but5");


init();
render();

function init() {

    // const viewport_container = document.createElement( 'div' );
    // document.body.appendChild( viewport_container );

    // document.querySelector("#main").appendChild( viewport_container );

    viewport_container = document.querySelector("#map-viewport_container");
    feature_container = document.querySelector("#map_container");

    camera = new THREE.PerspectiveCamera( 45, (viewport_container.offsetWidth - widthOffset) / viewport_container.offsetHeight, 0.25, 50 );
    // camera.position.set( - 1.8, 0.6, 2.7 );

    scene = new THREE.Scene();

    new RGBELoader()
        .setDataType( THREE.UnsignedByteType )
        .setPath( '../../../static/map/assets/environment/equirectangular/' ) // WE HAVE TO ACCESS [localhost_ip]:[port]/static/ URI TO ACCESS STATIC FILES
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

            const loader = new GLTFLoader().setPath( '../../../static/map/assets/models/gltf/library/' ); // WE HAVE TO ACCESS [localhost_ip]:[port]/static/ URI TO ACCESS STATIC FILES
            loader.load( 'library 0.3.glb', function ( gltf ) {

                gltf.scene.traverse( function ( child ) {

                    if ( child.isMesh ) {
                        child.castShadow = true;
                        // TOFIX RoughnessMipmapper seems to be broken with WebGL 2.0
                        // roughnessMipmapper.generateMipmaps( child.material );

                    }

                } );
                gltfRef = gltf;
                console.log("something happend");
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

    controls = new OrbitControls( camera, renderer.domElement );
    controls.addEventListener( 'change', render ); // use if there is no animation loop
    controls.minDistance = 2;
    controls.maxDistance = 10;

    camera.position.set( -4.7637, 7.0294, 11.6093);
    controls.target.set( 1.6273, 2.6682, 5.2742);

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
        moveCamera(9.1933, 2.8464, -2.4809);
        moveControl(3.5139, 0.1404, -8.3060);
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-1_description").innerHTML
    });
    
    button2.addEventListener( 'click', function() {
        moveCamera( 5.4523, 3.9139, 9.9887);
        moveControl(13.7424, -0.4472, 6.4881);
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-2_description").innerHTML
    });

    button3.addEventListener( 'click', function() {
        moveCamera( 1.2378, 3.2207, 3.2493);
        moveControl(-6.0162, -0.2606, 9.1871);
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-3_description").innerHTML
    });

    button4.addEventListener( 'click', function() {
        moveCamera( -3.7480, 2.8695, 3.9110);
        moveControl(1.7488, 0.6344, 11.9602);
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-4_description").innerHTML
    });

    button5.addEventListener( 'click', function() {
        moveCamera( -6.9277, 5.4110, 11.224);
        moveControl( 0.2764, 1.0498, 5.8317);
        document.querySelector("#description_container").innerHTML = document.querySelector("#area-5_description").innerHTML
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
    // controls.update();

    document.querySelector("#Cx").value="Cx: " +camera.position.x;
    document.querySelector("#Cy").value="Cy: " +camera.position.y;
    document.querySelector("#Cz").value="Cz: " +camera.position.z;

    document.querySelector("#Tx").value="Tx: " +controls.target.x;
    document.querySelector("#Ty").value="Ty: " +controls.target.y;
    document.querySelector("#Tz").value="Tz: " +controls.target.z;
}

function moveCamera(x, y, z){
    camera.position.set( x, y, z);

    console.log("camera moved @" +x +", " +y +", " +z);

    render();
}

function moveControl(x, y, z) {
    controls.target.set(x, y, z);
    console.log("target moved @" +x +", " +y +", " +z);

    render();
    controls.update();
}