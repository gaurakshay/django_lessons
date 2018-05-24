console.log(Math.random())
$(document).ready(function () {
    var $editForm = $("#courseForm");
    $editForm.submit(function (event) {
        event.preventDefault();
        var $formData = $(this).serialize();
        console.log($formData);
        $.ajax({
            method: "POST",
            url: '#',
            data: $formData,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data, textStatus, jqXHR) {
            $editForm[0].reset();
            $("#courseAddModal").modal('hide');
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
            var $obj = data['obj'];
            var $row = $("#courseList").prepend("<tr></tr>");
            $row.append("<td>" + data['dept']);
            $row.append("<td>" + $obj['course_num_code']);
            $row.append("<td>" + $obj['course_name']);
            $row.append("<td>" + $obj['course_seats']);
            $row.append("<td>" + $obj['course_description']);
            $row.append("<td><a class='btn btn-danger' data-name='" + $obj['course_name'] + "' data-pk='" +
                data['pk'] + "' data-toggle='modal' + data-target='#courseDeleteModal'>Delete</a></td>")
            // <td>
            //             <a class="btn btn-danger" data-name="{{ object }}" data-pk="{{ object.pk }}"
            //                data-toggle="modal" data-target="#courseDeleteModal">Delete</a>
            //         </td>
        }

        function handleError(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown)
        }
    });


    $('#courseDeleteModal').on('show.bs.modal', function (event) {
        let $link = $(event.relatedTarget); // link that triggered the event.
        $("#question").text("You're about to delete " + $link.data('name') + ". Please confirm.");
        $("#submit").attr('data-pk', $link.data('pk'));
        console.log($link.data('name'));
        console.log($link.data('pk'));
    });

    let $deleteForm = $("#courseDeleteForm");
    $deleteForm.submit(function (event) {
        event.preventDefault();
        let $id = $("#submit").attr('data-pk');
        console.log($id);
        var $formData = $(this).serialize();
        console.log($formData);
        $.ajax({
            method: "POST",
            url: $id + '/delete/',
            data: $formData,
            success: handleSuccess,
            error: handleError,
        });

        function handleSuccess(data, textStatus, jqXHR) {
            console.log("COURSE SUCCESSFULLY DELETED.");
            console.log("Hiding the modal.");
            $('#courseDeleteModal').modal('hide');

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