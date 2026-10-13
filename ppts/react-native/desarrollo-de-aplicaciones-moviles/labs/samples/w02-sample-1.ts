export type Status = 'draft' | 'pending' | 'synced';

export type Report = {
  id: string;
  title: string;
  category: string;
  status: Status;
  note?: string;
};

export const pending = (rs: Report[]) =>
  rs.filter(r => r.status === 'pending');

export const preview = (r: Report) =>
  r.note?.slice(0, 40) ?? '(sin nota)';
