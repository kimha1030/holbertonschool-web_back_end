import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleProfileSignup (firstName, lastName, fileName) {
  const prom1 = signUpUser(firstName, lastName);
  const prom2 = uploadPhoto(firstName, lastName);
  const elems = [prom1, prom2];
  return Promise.allSettled(elems)
    .then((response) => response);
}

export default handleProfileSignup;
