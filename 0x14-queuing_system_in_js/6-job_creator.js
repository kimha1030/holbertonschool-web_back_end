import kue from 'kue';

const queue = kue.createQueue();
// datos de ejm en intranet
const j = ({   
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account'
});
const q = 'push_notification_code';
const jobnot = queue.create(q, j).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${jobnot.id}`);
    }
});
jobnot.on('complete', () => {
    console.log('Notification job completed');
});

jobnot.on('failed', (err) => {
    console.log('Notification job failed');
});
