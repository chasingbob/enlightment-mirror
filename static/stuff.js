$(function(){
    $('#btnLightOn').click(function(){
        $.ajax({
            url: 'http://192.168.0.112:5000/IoT/ON',
            type: 'GET',
            error: function(error){
                console.log(error);
            }
        });
    });
});

$(function(){
    $('#btnLightOff').click(function(){
        $.ajax({
            url: 'http://192.168.0.112:5000/IoT/OFF',
            type: 'GET',
            error: function(error){
                console.log(error);
            }
        });
    });
});
