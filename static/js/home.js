function updateCountdown() {
  // Get all the countdown spans on the page
  const countdowns = document.querySelectorAll('.countdown');

  // Loop through each countdown span
  countdowns.forEach(countdown => {
    // Parse start time and duration values for this countdown
    const startTimeStr = countdown.parentElement.querySelector('.start-time').textContent;
    const durationStr = countdown.parentElement.querySelector('.duration').textContent;
    const dateStr = countdown.parentElement.querySelector('.date').textContent;
    
    const startDate = new Date(dateStr + ' ' + startTimeStr);
    const currentDate = new Date();

    const duration = durationStr.includes('days') ?
      parseInt(durationStr) * 24 * 60 * 60 * 1000 :
      parseInt(durationStr) * 60 * 60 * 1000;

    // Calculate the time left
    const endTime = new Date(startDate.getTime() + duration);
    const timeLeft = endTime - currentDate;

    const daysLeft = Math.floor(timeLeft / (24 * 60 * 60 * 1000));
    const hoursLeft = Math.floor((timeLeft % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
    const minutesLeft = Math.floor((timeLeft % (60 * 60 * 1000)) / (60 * 1000));
    const secondsLeft = Math.floor((timeLeft % (60 * 1000)) / 1000);

    // Update the countdown display
    countdown.textContent = `${daysLeft} days ${hoursLeft} hours ${minutesLeft} minutes ${secondsLeft} seconds`;
  });
}

// Call the updateCountdown function every second
setInterval(updateCountdown, 1000);