import { pending, type Report } from './report';

test('pending keeps only unsynced reports', () => {
  const rs: Report[] = [
    { id: '1', title: 'Fuga', category: 'facility',
      status: 'pending' },
    { id: '2', title: 'Lámpara', category: 'facility',
      status: 'synced' },
  ];
  expect(pending(rs).map(r => r.id)).toEqual(['1']);
});
