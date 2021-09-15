import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const prom1 = signUpUser(firstName, lastName);
  const prom2 = uploadPhoto(fileName);
  const elems = [prom1, prom2];
  const response = await Promise.allSettled(elems);
  return response;
}
