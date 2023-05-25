export interface Account {
  id: number;
  email: string;
  hashed_password: string;
  salt: string;
  username: string;
  createdAt: string;
  updatedAt: string;
  profile: Profile;
}

export interface Profile {
  id: number;
  account_id: number;
  firstName: string;
  lastName: string;
  account: Account;
}
