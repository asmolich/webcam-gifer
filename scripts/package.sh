#!env bash

# gather together all js

[[ ! -e target ]] && mkdir target 

cat src/js/*.js > target/app.js
cp manifest.json target/
cp templates/window.html target

# zip as mandated to call this a chrome package app


