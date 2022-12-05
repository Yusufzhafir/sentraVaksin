$(document).ready(function() {
   
    $(".button").click(function(){
        $.ajax({
            url: window.location.href,
            type:'POST',
            cache: false,
            data: $(".NakesForm").serialize(),
            success: function(response_ajax){
                $(".NakesForm")[0].reset();
                var event_data = '';
                // $.each(form)
                event_data += '<tr>';
                event_data += '<td>'+response_ajax['nama']+'</td>';
                event_data += '<td>'+response_ajax['umur']+'</td>';
                event_data += '<td>'+response_ajax['rumah_sakit']+'</td>';
                event_data += '<td>'+response_ajax['pendidikan']+'</td>';
                event_data += "<button class='button'><a href="+"'delete_nakes/"+response_ajax['id']+"'>Delete</a></button>";
                event_data += '</tr>';
                $("table").append(event_data);
                // $(".NakesForm").append("<span class='fail'>Invalid <img src='../image/success.png' alt='success icon'></span>")
                console.log({"condition":"success"})
            },
            error: function(){
                // $(".NakesForm").append("<span class='fail'>Invalid <img src='../image/fail.png' alt='fail icon'></span>")
                console.log({"condition":"fail"})
            } 
        });
    });
    
});