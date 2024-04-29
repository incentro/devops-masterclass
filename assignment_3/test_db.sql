--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2 (Ubuntu 16.2-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: col; Type: TABLE; Schema: public; Owner: username
--

CREATE TABLE public.col (
    words character varying(100)
);


ALTER TABLE public.col OWNER TO username;

--
-- Data for Name: col; Type: TABLE DATA; Schema: public; Owner: username
--

COPY public.col (words) FROM stdin;
THIS
IS
DEVOPS
\.


--
-- PostgreSQL database dump complete
--

