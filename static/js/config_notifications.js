/*
this function for bootstrap 5 and django framework messages, see template: in the end of function
*/
function makeNotification(
  bootstrap_icon,
  message_title,
  message_type,
  message_text,
  message_delay,
  progress_bar = false
) {
  $(document).ready(function () {
    $.notify(
      {
        // options
        icon: bootstrap_icon,
        title: message_title,
        message: message_text,
        url: "javascript:void(0)",
        target: "_self",
      },
      {
        // settings
        element: "body",
        position: null,
        type: message_type,
        allow_dismiss: true,
        newest_on_top: true,
        showProgressbar: progress_bar,
        placement: {
          from: "top",
          align: "center",
        },
        offset: 20,
        spacing: 10,
        z_index: 1031,
        delay: message_delay,
        timer: 1000,
        url_target: "_self",
        mouse_over: null,
        animate: {
          enter: "animated fadeInDown",
          exit: "animated fadeOutUp",
        },
        onShow: null,
        onShown: null,
        onClose: null,
        onClosed: null,
        icon_type: "class",
        template: `
        <div data-notify="container" class="alert alert-{0} col-xs-11 col-sm-3 col-md-6 col-lg-4 alert-dismissible" role="alert">
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
          <h4 class="alert-heading"><span data-notify="icon"></span> <span data-notify="title"></span> {1}</h4>
          <p data-notify="message">{2}</p>
          <hr>
          <div class="progress" style="height: 3px;" data-notify="progressbar">
            <div class="progress-bar bg-{0}" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0"
              aria-valuemax="100"></div>
          </div>
          <a href="{3}" target="{4}" data-notify="url"></a>
        </div>`,
      }
    );

    // Modify the exit button because the page orientation is from right to left
    $('.btn-close').css({'left':'10px','right':'', 'z-index': '1055'})

  });
}