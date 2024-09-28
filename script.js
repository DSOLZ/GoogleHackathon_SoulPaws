document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;
  
    if (name && email && message) {
      alert('Thank you for your message! We will get back to you soon.');
      // Here you could integrate the form submission with a service like Formspree, or a custom backend API.
      this.reset(); // Clear the form after submission
    } else {
      alert('Please fill out all fields before submitting.');
    }
  });
  