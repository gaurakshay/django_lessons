$(document).ready(function () {
    console.log(Math.random());

    //////////////////////////////////////
    // Handle adding another form.
    //////////////////////////////////////

    let $addBtn = $('#addBtn');
    $addBtn.click(function (event) {
        event.preventDefault();
        console.log("Prevented add");
        let $totalForms = parseInt($("#id_form-TOTAL_FORMS").val());
        console.log($totalForms);
        // Increment the total forms counter.

        $("#id_form-TOTAL_FORMS").val($totalForms + 1);
        $("#container").append($('#emptyForm').html().replace(/__prefix__/g, $totalForms));

    });


    let $deptForm = $('#deptForm');
    $deptForm.submit(function (event) {
        event.preventDefault();
        console.log("Default prevented.");
        let $formData = $(this).serialize();
        // Another way to do this:
        // let $ formData = new FormData($(this)[0]);

        $.ajax({
            method: "POST",
            url: "#",
            data: $formData,
            // processData: false, // This is useful when dealing with media.
            // contentType: false, // When dealing with media.
            success: handleSuccess,
            error: handleError,
        });


        function handleSuccess(data, textStatus, jqXHR) {
            console.log("SUCCESSFULLY ADDED#####!!.");

            // If successful, update the original count in the form management.
            let $initialForms = parseInt($("#id_form-INITIAL_FORMS").val());
            console.log($initialForms);
            // Increment the total forms counter.

            $("#id_form-INITIAL_FORMS").val($initialForms + 1);

            $('#formEnd').append("<div class=\"row\">\n" +
                "            <div class=\"alert alert-success\" id=\"addSuccess\">\n" +
                "                <strong>Success!</strong> Added successfully.\n" +
                "                <button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                "                    <span aria-hidden=\"true\">&times;</span>\n" +
                "                </button>\n" +
                "            </div>\n" +
                "        </div>"
            );

        }

        function handleError(jqXHR, textStatus, errorThrown) {
            console.log(jqXHR);
            console.log(textStatus);
            console.log(errorThrown)
        }


    })
});