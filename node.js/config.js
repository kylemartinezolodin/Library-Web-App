// NECCESARY IN MAP DEVELOPEMENT, DONT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING
const path = require('path');

module.exports = {
    entry: "../library_webapp/static/map/src/main.js",
    // mode: "development", // readable
    mode: "production", // minified
    output: {
        filename: "map.js",
        path: path.join(__dirname, "../library_webapp/static/map/js"),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                use: ["babel-loader"],
                exclude: /node_modules/
            },
        ],
    }
}