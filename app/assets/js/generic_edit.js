$(document).ready(function () {
    console.log(Math.random());
    var $editForm = $("#editForm");
    $editForm.submit(function (event) {
        event.preventDefault();
        // {#var $formData = $(this).serialize();#}
        // {#var $formData = new FormData($editForm);#}
        var $formData = new FormData($(this)[0]);
        console.log($formData);
        var $endPoint = $editForm.attr('data-url') || window.location.href;
        console.log($endPoint);
        $.ajax({
            method: "POST",
            url: $endPoint,
            data: $formData,
            processData: false,
            contentType: false,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data, textStatus, jqXHR) {
            console.log("SUCCESSFULLY ADDED#####!!.");
            // {#console.log(data);#}
            // {#console.log(textStatus);#}
            // {#console.log(jqXHR);#}

            $('#container').append("<h1>HOLY MACARONI THIS WORKED</h1>");

            console.log("Function fired.");
            $('.alert').show();

            console.log("Resetting the form.");
            $editForm[0].reset(); // reset form data

        }

        function handleError(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown)
        }
    });
});
