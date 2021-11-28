
/*
https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html
*/

// add django csrf token function
// csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var CSRF_TOKEN = getCookie("csrftoken");



$(document).ready(function () { // Start of jQuery

    // focus on first field when we open the modal form
    $("#createTicketModal").on("shown.bs.modal", function () {
        $("#id_car_owner_name").trigger("focus");
    });

    /*
    FIRST PHASE
    Preparing and processing the necessary data for the view,
    whether it is (creation, modification, deletion)
    */
    $('.edit-btn, .delete-btn, .create-btn').click(function () {
        let btnType = $(this).attr('data-req-type');
        let btnUrl = $(this).attr('data-req-url');
        if (btnType === 'POST') {
            // show modal create form
            $("#createTicketModal").modal("show");
            // add "req-create-btn" class to the submit button
            $('#submit-ticket-btn').removeClass('req-edit-btn').addClass('req-create-btn');
            // add atrribute "data-req-url" equal post to the submit button
            $('#submit-ticket-btn').attr({ 'data-req-type': 'POST' });
            // copy url from this button to submit button
            $('#submit-ticket-btn').attr({ 'data-req-url': btnUrl });

            $("#ticket_form").submit(function (e) {
                e.preventDefault();
            });
        }
        else if (btnType === 'PUT') {
            let btnUrl = $(this).attr('data-req-url');
            // show modal update form
            $("#createTicketModal").modal("show");
            // Request the contents of the fields and prepare them for modification
            $.ajax({
                type: 'GET', url: btnUrl, headers: { 'content-type': 'application/json', 'X-CSRFTOKEN': CSRF_TOKEN },
                success: function (response) {
                    console.log('successfully get PUT data')
                    // Fill in the fields with the data that was retrieved
                    $("#createTicketModal #id_car_owner_name").val(`${response['car_owner_name']}`);
                    $("#createTicketModal #id_owner_mobile_number").val(`${response['owner_mobile_number']}`);
                    $("#createTicketModal #id_national_identification_number").val(`${response['national_identification_number']}`);
                    $("#createTicketModal #id_driver_license_number").val(`${response['driver_license_number']}`);
                    $("#createTicketModal #id_car_manufacturer").val(`${response['car_manufacturer']}`);
                    $("#createTicketModal #id_car_model_year").val(`${response['car_model_year']}`);
                    $("#createTicketModal #id_car_model_name").val(`${response['car_model_name']}`);
                    $("#createTicketModal #id_car_registration_no").val(`${response['car_registration_no']}`);
                    $("#createTicketModal #id_car_color").val(`${response['car_color']}`);
                    $("#createTicketModal #id_car_chassis_no").val(`${response['car_chassis_no']}`);
                    $("#createTicketModal #id_reservation_time_per_day").val(`${response['reservation_time_per_day']}`);
                    $("#createTicketModal #id_parking_price_per_day").val(`${response['parking_price_per_day']}`);
                    $("#createTicketModal #id_position_number").val(`${response['position_number']}`);
                },
                error: function (xhr, status, error) {
                    console.log('failed to get PUT data')
                    var err = eval("(" + xhr.responseText + ")");
                    console.log(err.Message);
                }
            })
        }
        else if (btnType === 'DELETE') {
            // show modal delete confirmation
            $("#confirm-delete-modal").modal("show");
            // Fetch the delete message from the delete button
            let deleteMessage = $(this).attr("data-req-delete-message");
            $("#confirm-delete-modal .modal-body").text(`هل تريد حذف تذكرة ${deleteMessage} ؟`);
        }
    })

    /*
    SECOND PHASE
    Send the request data to the server and return the response
    */
    $("#ticket_form").submit(function (e) {
        e.preventDefault();
        $('.req-edit-btn, .req-delete-btn, .req-create-btn').click(function () {
            let btnType = $(this).attr('data-req-type');
            let btnUrl = $(this).attr('data-req-url');
            if (btnType === 'POST') {
                // show the loading Spinner

                // Disable the button to prevent the user from sending the request twice
                // $(this).attr('disable', true)

                // get the form fields data
                let serializedPostForm = $('#ticket_form').serialize();

                // post form data to server an wait for response
                $.ajax({
                    type: 'POST', url: btnUrl,
                    // headers: { 'content-type': 'application/json', 'X-CSRFTOKEN': CSRF_TOKEN },
                    data: serializedPostForm,
                    success: function (response) {
                        console.log('successfully get POST data')
                        // hide the loading Spinner

                        // clear fields for new ticket
                        $("#ticket_form").trigger("reset");

                        // hide the modal form after success
                        $("#createTicketModal").modal("hide");

                        // show success message (Notification)
                        makeNotification(
                            (bootstrap_icon = "far fa-check-circle"), (message_title = "تم"),
                            (message_type = "success"), (message_text = "تم انشاء التذكرة بنجاح"),
                            (message_delay = 4000), (progress_bar = true)
                        );


                    },
                    error: function (xhr, status, error) {
                        console.log('failed to get PUT data')
                        var err = eval("(" + xhr.responseText + ")");
                        console.log(err.Message);
                        // show Error message (Notification)
                        makeNotification(
                            (bootstrap_icon = "far fa-times-circle"), (message_title = "خطأ"),
                            (message_type = "danger"),
                            (message_delay = 4000), (progress_bar = true)
                            (message_text = `
                            تعذر انشاء تذكرة جديدة نظرا للخطأ التالي:
                            ${err.Message}`),
                        );
                    }
                }) // end of ajax
            }
            else if (btnType === 'PUT') {
            }
            else if (btnType === 'DELETE') {
            }
            //
        });
    })
}); // End of jQuery
