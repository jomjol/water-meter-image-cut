require('request');
const http = require('http');
const url = require('url');
const imageCut = require("./lib/lib_image_cut");
const fs = require('fs');

var abfrage = function(req, res) {
    var q = url.parse(req.url, true).query;
    var filename = q.url;

    if (filename)
    {
        console.log(filename);
        var file_download = fs.createWriteStream("./image_tmp/original.jpg");
        http.get(filename, (response) => {response.pipe(file_download);});

        file_download.on('finish', function(){
            file_download.end();

            imageCut.cutImage('./image_tmp', 'original.jpg').then(result => {
                res.writeHead(200, {'Content-Type': 'text/html'});
                var txt = "";
                txt += 'Original: <p><img src=/image_tmp/original.jpg></img><p>';
                txt += 'Rotate: <p><img src=/image_tmp/rot.jpg></img><p>';
                txt += 'Align: <p><img src=/image_tmp/alg.jpg></img><p>';
                txt += 'Counter: <p>'
                for (i = 0; i < result[1].length; ++i)
                {
                    name_zw = result[1][i].substring(1, result[1][i].length);
                    txt += '<img src='+  name_zw + '></img>      ';
                }
                txt += '<p>';
                txt += 'Analog Meter: <p>'
                for (i = 0; i < result[0].length; ++i)
                {
                    name_zw = result[0][i].substring(1, result[0][i].length);
                    txt += '<img src='+  name_zw + '></img>      ';
                }
                txt += '<p>';
                res.end(txt);}
                )
        });
    }

    if (req.url.indexOf('/image_tmp/') !== -1)
    {
        var s = fs.createReadStream("." + req.url);
        s.on('open', function () {
            res.setHeader('Content-Type', 'image/jpeg');
            s.pipe(res);
        });
    }
}

imageCut.init();

http.createServer(abfrage).listen(3000);
