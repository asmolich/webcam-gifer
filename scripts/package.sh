#!env bash

# frontens packaging
cd frontend
 
[[  -e target ]] && rm -rf target 

mkdir target 

cat src/ext-js/*.js > target/app.js
cp manifest.json target/
cp -dpR templates/* target
cp -dpR src/cli-js/* target/js

# zip as mandated to call this a chrome package app


# do backend package if needed


