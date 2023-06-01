    var profilePicture = document.querySelector('.profile-picture');
    var dropdownMenu = document.querySelector('.dropdown-menu');
    var timeout;

    profilePicture.addEventListener('mouseover', function() {
      clearTimeout(timeout);
      dropdownMenu.style.display = 'block';
    });

    profilePicture.addEventListener('mouseout', function() {
      timeout = setTimeout(function() {
        dropdownMenu.style.display = 'none';
      }, 200);
    });

    dropdownMenu.addEventListener('mouseover', function() {
      clearTimeout(timeout);
    });

    dropdownMenu.addEventListener('mouseout', function() {
      timeout = setTimeout(function() {
        dropdownMenu.style.display = 'none';
      }, 200);
    });


