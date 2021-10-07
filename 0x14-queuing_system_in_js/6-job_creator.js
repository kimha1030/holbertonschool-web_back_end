import kue from 'kue';

const queue = kue.createQueue();
const job = queue.create({
    phoneNumber: 'string',
    message: 'string'
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
