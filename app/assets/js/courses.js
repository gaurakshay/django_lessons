$(document).ready(function(){
    console.log('courses.js has been loaded.');
    $.ajax({
        type: "GET",
        url: "/mgmt/ajax_courses/",
        // url: "/mgmt/courses/",
    })
        .done(function(data){
            // console.log(data);

            $.each(data, function(index, val){
                $("#courseList").append("<li>" + val + "</li>");
               // console.log(val);
            });
        })
        .fail(function(xhr, status, errorThrown){
            console.log("Request failed.");
            console.log( "Error: " + errorThrown );
            console.log( "Status: " + status );
            console.dir( xhr );
        });


    $("#addCourse").click(function() {
        console.log("I PITY THE FOOL WHO CLICKED THIS BUTTON!!!");
    })
});