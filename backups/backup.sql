PGDMP  "    	                }         	   DevDirect    17.2    17.2 0    .           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            /           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            0           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            1           1262    24665 	   DevDirect    DATABASE     ~   CREATE DATABASE "DevDirect" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'French_France.1252';
    DROP DATABASE "DevDirect";
                     postgres    false            X           1247    24667    statut_concours    TYPE     K   CREATE TYPE public.statut_concours AS ENUM (
    'avenir',
    'passer'
);
 "   DROP TYPE public.statut_concours;
       public               postgres    false            �            1259    24671    clubs    TABLE     �   CREATE TABLE public.clubs (
    id integer NOT NULL,
    description text,
    site text,
    abreviation text NOT NULL,
    adresse text,
    public boolean,
    estactive boolean DEFAULT true,
    nom text NOT NULL
);
    DROP TABLE public.clubs;
       public         heap r       postgres    false            �            1259    24676    Clubs_id_seq    SEQUENCE     �   CREATE SEQUENCE public."Clubs_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public."Clubs_id_seq";
       public               postgres    false    217            2           0    0    Clubs_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public."Clubs_id_seq" OWNED BY public.clubs.id;
          public               postgres    false    218            �            1259    24677 
   categories    TABLE     s   CREATE TABLE public.categories (
    id integer NOT NULL,
    id_saison integer NOT NULL,
    nom text NOT NULL
);
    DROP TABLE public.categories;
       public         heap r       postgres    false            �            1259    24682    categories_id_seq    SEQUENCE     �   CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.categories_id_seq;
       public               postgres    false    219            3           0    0    categories_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;
          public               postgres    false    220            �            1259    24683    concours    TABLE     b  CREATE TABLE public.concours (
    id integer NOT NULL,
    nom character varying(255) NOT NULL,
    description text,
    debut timestamp without time zone NOT NULL,
    fin timestamp without time zone NOT NULL,
    lieu character varying(255) NOT NULL,
    statut public.statut_concours NOT NULL,
    CONSTRAINT concours_check CHECK ((debut < fin))
);
    DROP TABLE public.concours;
       public         heap r       postgres    false    856            �            1259    24689    concours_id_seq    SEQUENCE     �   CREATE SEQUENCE public.concours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.concours_id_seq;
       public               postgres    false    221            4           0    0    concours_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.concours_id_seq OWNED BY public.concours.id;
          public               postgres    false    222            �            1259    24690    participants    TABLE     B  CREATE TABLE public.participants (
    id integer NOT NULL,
    concours_id integer NOT NULL,
    utilisateur_id integer NOT NULL,
    resultat7 integer,
    resultat12 integer,
    CONSTRAINT participants_resultat12_check CHECK ((resultat12 >= 0)),
    CONSTRAINT participants_resultat7_check CHECK ((resultat7 >= 0))
);
     DROP TABLE public.participants;
       public         heap r       postgres    false            �            1259    24695    participants_id_seq    SEQUENCE     �   CREATE SEQUENCE public.participants_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.participants_id_seq;
       public               postgres    false    223            5           0    0    participants_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.participants_id_seq OWNED BY public.participants.id;
          public               postgres    false    224            �            1259    24696    saisons    TABLE     �   CREATE TABLE public.saisons (
    id_utilisateur integer NOT NULL,
    id_categorie integer NOT NULL,
    id_saison integer NOT NULL,
    id_club integer
);
    DROP TABLE public.saisons;
       public         heap r       postgres    false            �            1259    24699    utilisateurs    TABLE     �  CREATE TABLE public.utilisateurs (
    id integer NOT NULL,
    nom character varying(255) NOT NULL,
    prenom character varying(255) NOT NULL,
    mdp character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    date_inscription date DEFAULT CURRENT_TIMESTAMP,
    date_naissance date,
    club integer,
    CONSTRAINT utilisateurs_email_check CHECK ((char_length((email)::text) > 0))
);
     DROP TABLE public.utilisateurs;
       public         heap r       postgres    false            �            1259    24706    utilisateurs_id_seq    SEQUENCE     �   CREATE SEQUENCE public.utilisateurs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.utilisateurs_id_seq;
       public               postgres    false    226            6           0    0    utilisateurs_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.utilisateurs_id_seq OWNED BY public.utilisateurs.id;
          public               postgres    false    227            t           2604    24707    categories id    DEFAULT     n   ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);
 <   ALTER TABLE public.categories ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    220    219            r           2604    24708    clubs id    DEFAULT     f   ALTER TABLE ONLY public.clubs ALTER COLUMN id SET DEFAULT nextval('public."Clubs_id_seq"'::regclass);
 7   ALTER TABLE public.clubs ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    217            u           2604    24709    concours id    DEFAULT     j   ALTER TABLE ONLY public.concours ALTER COLUMN id SET DEFAULT nextval('public.concours_id_seq'::regclass);
 :   ALTER TABLE public.concours ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    222    221            v           2604    24710    participants id    DEFAULT     r   ALTER TABLE ONLY public.participants ALTER COLUMN id SET DEFAULT nextval('public.participants_id_seq'::regclass);
 >   ALTER TABLE public.participants ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    224    223            w           2604    24711    utilisateurs id    DEFAULT     r   ALTER TABLE ONLY public.utilisateurs ALTER COLUMN id SET DEFAULT nextval('public.utilisateurs_id_seq'::regclass);
 >   ALTER TABLE public.utilisateurs ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    227    226            #          0    24677 
   categories 
   TABLE DATA           8   COPY public.categories (id, id_saison, nom) FROM stdin;
    public               postgres    false    219   �8       !          0    24671    clubs 
   TABLE DATA           d   COPY public.clubs (id, description, site, abreviation, adresse, public, estactive, nom) FROM stdin;
    public               postgres    false    217   9       %          0    24683    concours 
   TABLE DATA           R   COPY public.concours (id, nom, description, debut, fin, lieu, statut) FROM stdin;
    public               postgres    false    221   m9       '          0    24690    participants 
   TABLE DATA           ^   COPY public.participants (id, concours_id, utilisateur_id, resultat7, resultat12) FROM stdin;
    public               postgres    false    223   �9       )          0    24696    saisons 
   TABLE DATA           S   COPY public.saisons (id_utilisateur, id_categorie, id_saison, id_club) FROM stdin;
    public               postgres    false    225   �9       *          0    24699    utilisateurs 
   TABLE DATA           k   COPY public.utilisateurs (id, nom, prenom, mdp, email, date_inscription, date_naissance, club) FROM stdin;
    public               postgres    false    226   �9       7           0    0    Clubs_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."Clubs_id_seq"', 28, true);
          public               postgres    false    218            8           0    0    categories_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.categories_id_seq', 1, false);
          public               postgres    false    220            9           0    0    concours_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.concours_id_seq', 1, false);
          public               postgres    false    222            :           0    0    participants_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.participants_id_seq', 1, false);
          public               postgres    false    224            ;           0    0    utilisateurs_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.utilisateurs_id_seq', 1, false);
          public               postgres    false    227            ~           2606    24713    clubs Clubs_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT "Clubs_pkey" PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.clubs DROP CONSTRAINT "Clubs_pkey";
       public                 postgres    false    217            �           2606    24715    categories categories_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.categories DROP CONSTRAINT categories_pkey;
       public                 postgres    false    219            �           2606    24717    concours concours_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.concours
    ADD CONSTRAINT concours_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.concours DROP CONSTRAINT concours_pkey;
       public                 postgres    false    221            �           2606    24719 8   participants participants_concours_id_utilisateur_id_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.participants
    ADD CONSTRAINT participants_concours_id_utilisateur_id_key UNIQUE (concours_id, utilisateur_id);
 b   ALTER TABLE ONLY public.participants DROP CONSTRAINT participants_concours_id_utilisateur_id_key;
       public                 postgres    false    223    223            �           2606    24721    participants participants_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.participants
    ADD CONSTRAINT participants_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.participants DROP CONSTRAINT participants_pkey;
       public                 postgres    false    223            �           2606    24743    clubs unique_name 
   CONSTRAINT     X   ALTER TABLE ONLY public.clubs
    ADD CONSTRAINT unique_name UNIQUE (nom, abreviation);
 ;   ALTER TABLE ONLY public.clubs DROP CONSTRAINT unique_name;
       public                 postgres    false    217    217            �           2606    24723 #   utilisateurs utilisateurs_email_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT utilisateurs_email_key UNIQUE (email);
 M   ALTER TABLE ONLY public.utilisateurs DROP CONSTRAINT utilisateurs_email_key;
       public                 postgres    false    226            �           2606    24725    utilisateurs utilisateurs_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT utilisateurs_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.utilisateurs DROP CONSTRAINT utilisateurs_pkey;
       public                 postgres    false    226            �           2606    24726    utilisateurs fk_club    FK CONSTRAINT     z   ALTER TABLE ONLY public.utilisateurs
    ADD CONSTRAINT fk_club FOREIGN KEY (club) REFERENCES public.clubs(id) NOT VALID;
 >   ALTER TABLE ONLY public.utilisateurs DROP CONSTRAINT fk_club;
       public               postgres    false    226    4734    217            �           2606    24731 *   participants participants_concours_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.participants
    ADD CONSTRAINT participants_concours_id_fkey FOREIGN KEY (concours_id) REFERENCES public.concours(id) ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.participants DROP CONSTRAINT participants_concours_id_fkey;
       public               postgres    false    223    4740    221            �           2606    24736 -   participants participants_utilisateur_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.participants
    ADD CONSTRAINT participants_utilisateur_id_fkey FOREIGN KEY (utilisateur_id) REFERENCES public.utilisateurs(id) ON DELETE CASCADE;
 W   ALTER TABLE ONLY public.participants DROP CONSTRAINT participants_utilisateur_id_fkey;
       public               postgres    false    223    4748    226            #      x������ � �      !   Y   x�32�,.L),N�QH��4N����|.#0#�3�,ę�b��q���R�fP�gZJzJZ:gZzJ:�4 ��jBR�K�b���� <�.�      %      x������ � �      '      x������ � �      )      x������ � �      *      x������ � �     