$("#buttonTest").click(function () {
    let data = JSON.stringify({test: "test"})
    let target = "test"
    let dataType = "text"
    let port = 9000
    doPostJSON(data, target, dataType, onFinish, port)
});

function onFinish(data) {
    alert(JSON.stringify(data))
}

function doPostJSON(data, target, dataType, onFinish, port) {
    // Maybe change this design. This is the solution to the problem of the asynchronous with utils.
    var BACKEND_FILE_PORTS = [port];
    var backendPort = getParameterByName("backend"); // in utils.js
    if (!backendPort)
        backendPort = BACKEND_FILE_PORTS[Math.floor(Math.random() * BACKEND_FILE_PORTS.length)];
    var httpurl = "http://" + location.hostname + ":" + backendPort + "/"
    $.ajax({
        xhr: function () { // Seems like the only way to get access to the xhr object
            var xhr = new XMLHttpRequest();
            xhr.responseType = ''
            return xhr;
        },
        url: httpurl + target + "/",
        type: "POST",
        contentType: 'application/json',
        data: data,
        dataType: dataType,
        complete: function (xmlHttp) {
            handleStatus(xmlHttp.status)
        }
    }).done(function (data) {
        onFinish(data)
    });
}

/**
 * From https://stackoverflow.com/a/901144/827927
 */
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}


function handleStatus(status) {
    alert(status)
    if (status == 404) {
        top.location.href = 'index.html';
    }
    if (status == 403) {
        alert("The pdf file is too large, please upload a smaller file.")
    }
    if (status != 200) {
        alert("An error occured.")
        location.reload()
    }
}