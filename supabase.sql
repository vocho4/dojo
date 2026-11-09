-- Spusť v Supabase: SQL Editor -> New query -> Run.
create table if not exists public.attempts (
  id bigint generated always as identity primary key,
  kid text not null check (kid in ('Matěj','Jáchym','Nikola')),
  lesson_id text not null,
  score int not null check (score >= 0),
  total int not null check (total > 0),
  ts timestamptz not null default now()
);

alter table public.attempts enable row level security;

-- Stránka smí výsledky číst a přidávat, ne upravovat ani mazat.
create policy "read attempts" on public.attempts for select to anon using (true);
create policy "add attempts" on public.attempts for insert to anon with check (score <= total);
