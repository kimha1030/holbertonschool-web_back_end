import kue from 'kue';

const queue = kue.createQueue();
queue.process('push_notification_code', (j, done) => {
    sendNotification(j.data.phoneNumber, j.data.message);
    done();
});

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
