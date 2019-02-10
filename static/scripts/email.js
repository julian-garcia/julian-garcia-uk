(function(){
  emailjs.init("user_8shMJUINo0KL7dSFJ32hD");
})();

document.addEventListener('DOMContentLoaded', sendemail);

function sendemail() {
  const email_form = document.getElementById('email-form');

  email_form.addEventListener('submit', event => {
    event.preventDefault();

    const template_params = {
      "reply_to": document.getElementById('id_email_address').value,
      "from_name": "Enquiry",
      "to_name": "Julian",
      "message_html": document.getElementById('id_message').value
    }
   
    const service_id = "default_service";
    const template_id = "julian-garcia.uk";
    emailjs.send(service_id, template_id, template_params);

    const confirm_message = document.createElement('h3');
    const confirm_message_txt = document.createTextNode('Thank you for your message, I will be sure to get back to you');
    confirm_message.appendChild(confirm_message_txt);
    email_form.insertAdjacentElement('beforebegin', confirm_message);
    email_form.reset();
    email_form.remove();

    return false;
  });
}