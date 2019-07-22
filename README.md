# water-meter-image-cut
 
This repository shows an option to cut an image in sub pieces. 

To run the node.js code copy the whole [code](code) directory including subdirectory.

Path are relative, so it should run immediatly with the following command:
* `node water-meter-image-cut.js`

### Remarks
* Python assumes some libraries to be installed using `pip install`:
	* `opencv4nodejs`
	* `ini`
	
### Server Usage

To run the node.js code copy the whole [code](code) directory including subdirectory.

Path are relative, so it should run immediatly with the following command:
* `node water-meter-image-cut.js`



The server is listening to port 3000 and accepts requests in the following syntac:

http://server-ip:3000/?url=http://picture-server/image.jpg

* server-ip: address of the node-server running the script
* parameter "url": url to the picture to be analysed 

The output is the following:

   <img src="./image/server_output.jpg" width="400">
   


