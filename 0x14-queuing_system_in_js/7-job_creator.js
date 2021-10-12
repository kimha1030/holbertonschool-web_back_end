import kue from 'kue';

const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
];

const queue = kue.createQueue();
jobs.forEach((elem) => {
  const q = 'push_notification_code_2';
  const jobnot = queue.create(q, elem).save((err) => {
    if (!err) console.log(`Notification job created: ${jobnot.id}`);
  });
  jobnot.on('complete', () => {
    console.log(`Notification job ${jobnot.id} completed`);
  });
  jobnot.on('failed', (err) => {
    console.log(`Notification job ${jobnot.id} failed: ${err}`);
  });
  jobnot.on('progress', (porcent) => {
    console.log(`Notification job ${jobnot.id} ${porcent}% complete`);
  });
});
