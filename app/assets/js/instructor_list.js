$(document).ready(function () {
    console.log(Math.random());
    $('#instructorDeleteModal').on('show.bs.modal', function (event) {
        var $link = $(event.relatedTarget); // link that triggered the event.
        $("#question").text("You're about to delete " + $link.attr('data-name') + ". Please confirm.");
        $("#submit").attr('data-pk', $link.data('pk'));
        console.log($link.data('name'));
        console.log($link.data('pk'));
    });


    $("#instructorDeleteForm").submit(function (event) {
        event.preventDefault();
        console.log('submit clicked');
        //let $id = $("#submit").data('pk'); // This sucks because it doesn't update values
        // once the values change as I do in the #instructor delete modal show.bs.modal function
        // above.
        let $id = $("#submit").attr('data-pk');
        console.log($id);
        let $data = $(this).serialize();
        $.ajax({
            method: "POST",
            url: $id + "/delete/",
            data: $data,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data, textStatus, jqXHR) {
            console.log("SUCCESSFULLY DELETED INSTRUCTOR.");
            console.log("Hiding the modal.");
            $('#instructorDeleteModal').modal('hide');

            console.log("Removing the deleted entry from the table.");
            $('#row' + data['pk']).remove();
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        }

        function handleError(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown)
        }
    });
});
