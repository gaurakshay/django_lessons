$(document).ready(function () {
        console.log(Math.random());
        var $instructor_form = $('#instructorForm');
        // {#$('#submit').on('click', function (e) {#}
        $instructor_form.submit(function (event) {
            event.preventDefault();
            // {#var $data = $instructor_form.serialize();#}
            var $data = $(this).serialize();
            $.ajax({
                method: 'POST',
                url: '{% url "instructor_edit" pk=object.pk %}',
                data: $data,
                success: handleSuccess,
                error: handleError,
            });

            function handleSuccess(data, textStatus, jqXHR) {
                console.log("SUCCESSFULLY EDITED INSTRUCTOR.");
                console.log(data);
                console.log(textStatus);
                console.log(jqXHR);
                $("#instructorEditModal").modal('hide');
                console.log("Emptying the instructor's data");
                var $instructorDetails = $('#instructorDetails');
                $instructorDetails.empty();
                $instructorDetails.append("Name: <h5>" + data['name'] + "</h5>");
                $instructorDetails.append("Courses offered: <h5>" + data['courses'] + "</h5>");

                // {#$editForm[0].reset(); // reset form data#}
            }

            function handleError(jqXHR, textStatus, errorThrown) {
                console.log("INSTRUCTOR EDIT FAILED.");
                console.log(jqXHR);
                console.log(textStatus);
                console.log(errorThrown)
            }

            return false;
        });
    }
);
