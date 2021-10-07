import kue from 'kue';

const queue = kue.createQueue();
const job = queue.create({
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
});
const queuenot = 'push_notification_code';
const jobnot = queue.create(queuenot, job).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});
jon.on('completed', () => {
    console.log('Notification job completed');
});

jon.on('failed', (err) => {
    console.log('Notification job failed');
});
