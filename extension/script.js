document.addEventListener('mouseup',function(event)
{
    var sel = window.getSelection();
    var selTxt = sel.toString();
    var interval;

    if (selTxt.length) {
        chrome.runtime.sendMessage({'message':'setText','data': selTxt},function(response){});
        console.log(sel);
        console.log(selTxt);
        $.ajax("https://swaggerui.ai-made-ez.com/alpc", {
        // $.ajax("http://localhost:5000/alpc", {
            "method": "POST",
            "data": JSON.stringify({
                "text": selTxt
            }),
            "dataType": "json",
            "contentType": "application/json",
            "success": function(data) {
                console.log(data);
                $('#alpcDialog').remove();
                document.body.innerHTML += '<dialog id="alpcDialog"><h1>'+selTxt+'</h1><div id="alpcContent"></div><br><button>Close</button></dialog>';
                $('#alpcContent').append($('<img id="alpcFace" />'));
                $('#alpcContent').append($('<img id="alpcHand" />'));
                var dialog = document.querySelector("dialog")
                var images = []
                var imagesMains = []
                var positionsMains = []
                var img = new Image()

                $(data).each(function(elemId, elem){
                    $(elem[1]).each(function(visemId, visem){
                        imagesMains.push(chrome.runtime.getURL('img/mainsLPC/'+elem[0][0]+'.png'))
                        img.src=chrome.runtime.getURL('img/mainsLPC/'+elem[0][0]+'.png')
                        positionsMains.push(elem[0][1]);
                        visemCode = visem
                        if (visem == visem.toUpperCase()) {
                            visemCode+='maj'
                        }
                        images.push(chrome.runtime.getURL('img/visages/'+visemCode+'.png'));
                        img.src=chrome.runtime.getURL('img/visages/'+visemCode+'.png');
                    })
                })

                currentImageIndex = 0
                console.log(images, imagesMains, positionsMains)
                interval = setInterval(function(){
                    if (currentImageIndex == images.length) {
                        clearInterval(interval);
                        return;
                    }
                    $('#alpcHand').hide()
                    $('#alpcHand').attr('src', imagesMains[currentImageIndex])
                    console.log(imagesMains[currentImageIndex]);
                    $('#alpcHand').removeClass('pos-P pos-C pos-B pos-M pos-G')
                    $('#alpcHand').addClass('pos-'+positionsMains[currentImageIndex])
                    console.log('pos-'+positionsMains[currentImageIndex])
                    $('#alpcHand').show()
                    $('#alpcFace').attr('src', images[currentImageIndex])
                    console.log(images[currentImageIndex])
                    currentImageIndex++;
                }, 500)

                dialog.querySelector("button").addEventListener("click", function() {
                    dialog.close()
                })
                dialog.showModal()
                console.log($('#alpcDialog'));
            },
            "error": function(xhr, status, err) {
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        })
    }
})
