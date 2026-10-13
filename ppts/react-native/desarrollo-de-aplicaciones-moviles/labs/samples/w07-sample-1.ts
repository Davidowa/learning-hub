import { create } from 'zustand';

type ReportState = {
  reports: Report[];
  add: (r: Report) => void;
  remove: (id: string) => void;
};

export const useReports = create<ReportState>()(set => ({
  reports: [],
  add: r => set(s => ({ reports: [...s.reports, r] })),
  remove: id => set(s => ({
    reports: s.reports.filter(r => r.id !== id) })),
}));
