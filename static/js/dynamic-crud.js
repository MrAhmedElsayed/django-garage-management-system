/*
https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html
*/


$(document).ready(function () {
	// start jQuery

	// Ajaxify Forms
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
		beforeSend: function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	// ---------------------------------------- START ------------------------------------------------------

	// focus on first field when we open the modal form
	$("#modal-ticket").on("shown.bs.modal", function () {
		$("#id_car_owner_name").trigger("focus");
	});

	/* Functions */

	const form_html = $('#modal-ticket .tab-content');

	console.log(form_html)

	var loadCreateForm = function () {  // Create
		$("#modal-ticket").modal("show");
		let btnUrl = $(".create-ticket").attr("data-url");
		$(".submit-btn").attr({ "data-request-url": btnUrl, 'data-request-method': 'post' });
		$("#ticket-form-body").attr('class', 'js-ticket-create-form')
		$("#ticket-form-body").trigger("reset");
	}

	var loadDeleteForm = function () {  // delete
		console.log("fire")
		$("#delete-modal").modal("show");
		let btnUrl = $(this).attr("data-delete-url");

		// get delete message
		let delete_message = $(this).attr("data-delete-name");
		$(".delete-message-p").text(delete_message);

		$(".submit-btn").attr({ "data-request-url": btnUrl, 'data-request-method': 'delete' });
		$(".ticket-form-body").attr('class', 'js-ticket-delete-form')
	}

	var loadPutForm = function () {  // Put
		$("#modal-ticket").modal("show");
		
		$('.tab-content').show();
		
		// $('.tab-content').html(``);
		$('.modal-content').html(`${form_html.html()}`); // style and right select

		alert($('.tab-content').html(`${form_html}`))

		let updateBtnUrl = $(this).attr("data-update-url");
		$(".submit-btn").attr({ "data-request-url": updateBtnUrl, 'data-request-method': 'put' });
		$("#ticket-form-body").attr('class', 'js-ticket-update-form')

		$.ajax({
			type: 'GET',
			url: updateBtnUrl,
			success: function (response) {
				console.log('successfully get (PUT data)')
				// Fill in the fields with the data that was retrieved
				$("#modal-ticket #id_car_owner_name").val(`${response['car_owner_name']}`);
				$("#modal-ticket #id_owner_mobile_number").val(`${response['owner_mobile_number']}`);
				$("#modal-ticket #id_national_identification_number").val(`${response['national_identification_number']}`);
				$("#modal-ticket #id_driver_license_number").val(`${response['driver_license_number']}`);
				$("#modal-ticket #id_car_manufacturer").val(`${response['car_manufacturer']}`);
				$("#modal-ticket #id_car_model_year").val(`${response['car_model_year']}`);
				$("#modal-ticket #id_car_model_name").val(`${response['car_model_name']}`);
				$("#modal-ticket #id_car_registration_no").val(`${response['car_registration_no']}`);
				$("#modal-ticket #id_car_color").val(`${response['car_color']}`);
				$("#modal-ticket #id_car_chassis_no").val(`${response['car_chassis_no']}`);
				$("#modal-ticket #id_reservation_time_per_day").val(`${response['reservation_time_per_day']}`);
				$("#modal-ticket #id_parking_price_per_day").val(`${response['parking_price_per_day']}`);
				$("#modal-ticket #id_position_number").val(`${response['position_number']}`);
			},
			error: function (xhr, status, error) {
				console.log('failed to get (PUT data)')
				var err = eval("(" + xhr.responseText + ")");
				console.log(err.Message);
			}
		});
	};

	var saveForm = function () {  // save POST and PUT
		var form = $('#ticket-form-body');
		var submit_btn = $('#ticket-form .submit-btn')
		
		if (submit_btn.attr("data-request-method") === 'delete') {
			form = $('#ticket-form-delete');
		}
		$.ajax({
			url: submit_btn.attr("data-request-url"),
			data: form.serialize(),
			type: submit_btn.attr("data-request-method"),
			dataType: 'json',
			success: function (data) {
				if (submit_btn.attr("data-request-method") === 'delete') {
					$("#delete-modal").modal("hide");
				}
				// check for post request to show QR and print PDF link
				else if (submit_btn.attr("data-request-method") === 'post' || 'put') {
					// e.preventDefault();
					$.ajax({
						url: submit_btn.attr("data-qr-generator"),
						data: {
							'operation': "generate_qr",
							'qr_text': `http://127.0.0.1:8000/pdf/${data.id}/`
							//'qr_text': `http://192.168.8.116:8000/pdf/${data.id}/`
						},
						type: 'post',
						dataType: 'json',

						success: function (response) {
							// $("#modal-ticket .modal-body").html(response.svg);
							
							$('.tab-content').hide();

							$("#modal-ticket .qr-content").html(`
							<!--Header-->
							<div class="modal-header d-flex justify-content-center pt-1 pb-0">
								<p class="heading mt-1">من فضلك افحص الكود للحصول علي التذكرة الالكترونية</p>
							</div>
				
							<!--Body-->
							<div class="modal-body">
				
								<div class="qr-div d-flex justify-content-center">
									${response.svg}
								</div>
				
								<table class="table table-bordered table-success">
									
									<tbody>
									  <tr>
										<th scope="row">الاسم</th>
										<td>${data.car_owner_name}</td>
										<th scope="row">السيارة</th>
										<td>${data.car_model_name} - ${data.car_model_year}</td>
									  </tr>
									</tbody>
								  </table>
				
								<div class="alert alert-warning" role="alert">
									<i class="fa fa-exclamation-triangle mr-3"></i>
									عند فحص العميل الكود سيتم السؤال عن رقم جواله !!
								</div>
				
							</div>
				
							<!--Footer-->
							<div class="modal-footer flex-center justify-content-around">
								<a type="button" class="btn btn-outline-info" data-dismiss="modal">تراجع</a>
								<a href="http://127.0.0.1:8000/pdf/${data.id}/" target="_blank" class="btn btn-info">طباعة التذكرة</a>
							</div>
						</div>`);
						},
						error: function (xhr, status, error) {
							console.log('Request Failed')
							var err = eval("(" + xhr.responseText + ")");
							console.log(err.Message);
						}
					})

				} else {
					form.trigger("reset");
					$("#modal-ticket").modal("hide");
					submit_btn.attr({ "data-request-url": "", "data-request-method": "" })
					form.attr('class', '')
				}
				// window.location.reload();
			},
			error: function (xhr, status, error) {
				console.log('Request Failed')
				var err = eval("(" + xhr.responseText + ")");
				console.log(err.Message);
			}
		});
		return false;
	};


	/* ------------------ Binding ------------------ */

	// Create ticket
	$(".create-ticket").click(loadCreateForm);
	$("#modal-ticket").on("submit", ".js-ticket-create-form", saveForm);

	// Update ticket
	$("#dataTable").on("click", ".js-update-ticket", loadPutForm);
	$("#modal-ticket").on("submit", ".js-ticket-update-form", saveForm);

	// Delete ticket
	$("#dataTable").on("click", ".js-delete-ticket", loadDeleteForm);
	$("#delete-modal").on("submit", ".js-ticket-delete-form", saveForm);

	// end jQuery
})



