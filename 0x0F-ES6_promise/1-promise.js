export default function getFullResponseFromAPI (sucess) {
  return new Promise((resolve, reject) => {
    if (sucess) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
