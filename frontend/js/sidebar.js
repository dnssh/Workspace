$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#sidebar-inv').toggleClass('active');
        $(this).toggleClass('active');
    });
});
$(document).ready(function () {
    $(".new").keyup(function () {
      if($(".new").val() != "") {
          $('.post-btn').removeClass('hidden');
      } else {
        $('.post-btn').addClass('hidden');
      }
    });
  });

  $(document).ready(function () {
    $('#postit').on('click', function () {
        $('#secret').toggleClass('dontShow');
        $(".new").val('');
    });
});


$(document).ready(function () {
  $('#theBox').on('click', function () {
      $('#theTask').toggleClass('dontShow');
      $('#theTask2').toggleClass('dontShow');

  });
});