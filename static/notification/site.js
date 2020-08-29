const pushForm = document.querySelector('form');
//const errorMsg = document.querySelector('.error');

pushForm.addEventListener('submit', async function(e) {
    const input = this[1];
    const textarea = this[2];
    const button = this[3];
    //errorMsg.innerText = '';

    const head = input.value;
    const body = textarea.value;
    const meta = document.querySelector('meta[name="user_id"]');
    const id = meta ? meta.content : null;

    if (head && body && id) {
        button.innerText = 'Sending Notification';
        button.disabled = true;

        const res = await fetch('send_push/', {
            method: 'POST',
            body: JSON.stringify({ head, body, id }),
            headers: {
                'content-type': 'application/json'
            }
        });
        if (res.status === 200) {
            button.innerText = 'POST';
            button.disabled = false;
            input.value = '';
            textarea.value = '';
        } else {
            //errorMsg.innerText = res.message;
            button.innerText = 'Something broke 😢..  Try again?';
            button.disabled = false;
        }
    }
});