self.addEventListener('push', function(event) {
    const eventInfo = event.data.text();
    const data = JSON.parse(eventInfo);
    const head = data.head;
    const body = data.body;
    console.log('notification received')
    event.waitUntil(
        self.registration.showNotification(head, {
            body: body,
            icon: src = '/media/first/logo.png'
        })
    );
});

self.addEventListener('notificationclick', function(event) {

    event.notification.close();

    event.waitUntil(
        clients.openWindow('http://127.0.0.1:8000')
    );
});