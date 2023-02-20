CREATE TABLE Genre
(
    genre_id     int auto_increment,
    genre_name   varchar(255) NOT NULL,
    genre_launch int          NOT NULL,

    PRIMARY KEY (genre_id)
);


CREATE TABLE Streaming
(
    streaming_id      int auto_increment,
    streaming_name    varchar(255) NOT NULL,
    total_tracks_mlns int          NOT NULL,
    active_users_mlns int          NOT NULL,
    paying_users_mlns int          NOT NULL,
    launch            int          NOT NULL,

    PRIMARY KEY (Streaming_id)
);

CREATE TABLE General
(
    general_id            int auto_increment,
    age                   int,
    streaming_id          int,
    hours_per_day         decimal(8, 2),
    while_working         varchar(255),
    instrumentalist       varchar(255),
    composer              varchar(255),
    exploratory           varchar(255),
    foreign_languages     varchar(255),
    bpm                   int,
    genre_id              int,
    freq_classical        varchar(255),
    freq_country          varchar(255),
    freq_edm              varchar(255),
    freq_folk             varchar(255),
    freq_gospel           varchar(255),
    freq_hiphop           varchar(255),
    freq_jazz             varchar(255),
    freq_kpop             varchar(255),
    freq_latin            varchar(255),
    freq_lofi             varchar(255),
    freq_metal            varchar(255),
    freq_pop              varchar(255),
    freq_rnB              varchar(255),
    freq_rap              varchar(255),
    freq_rock             varchar(255),
    freq_video_game_music varchar(255),
    anxiety               int,
    depression            int,
    insomnia              int,
    OCD                   int,
    music_effect          varchar(255),

    PRIMARY KEY (general_id),
    FOREIGN KEY (streaming_id) REFERENCES Streaming (streaming_id),
    FOREIGN KEY (genre_id) REFERENCES Genre (genre_id)
);

/*========================Insert the data into the tables=================================*/
-- Insert into Genre
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (1, 'Latin', 1600);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (2, 'Rock', 1950);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (3, 'Video game music', 1970);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (4, 'Jazz', 1910);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (5, 'R&B', 1980);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (6, 'K pop', 1990);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (7, 'Country', 1920);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (8, 'EDM', 1975);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (9, 'Hip hop', 1979);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (10, 'Pop', 1950);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (11, 'Rap', 1970);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (12, 'Metal', 1970);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (13, 'Classical', 1400);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (14, 'Folk', 1980);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (15, 'Lofi', 1990);
INSERT INTO Genre (genre_id, genre_name, genre_launch) VALUES (16, 'Gospel', 1930);

-- Insert into Streaming
INSERT INTO Streaming (Streaming.streaming_name,
                       Streaming.total_tracks_mlns, Streaming.active_users_mlns,
                       Streaming.paying_users_mlns, Streaming.launch)
VALUES
    ('Apple Music', 100, 88, 88, 2015),
    ('Pandora', 30, 58, 6, 2005),
    ('Spotify', 100, 422, 182, 2008),
    ('YouTube Music', 100, 80, 80, 2015);


INSERT INTO Streaming (streaming_name, total_tracks_mlns, active_users_mlns, paying_users_mlns, launch)
VALUES ('I do not use a streaming service', 0, 0, 0, 0),
       ('Other streaming service', 0, 0, 0, 0);



-- Insert into General
INSERT INTO General (General.streaming_id, General.genre_id, General.age,
                     General.hours_per_day, General.while_working, General.instrumentalist,
                     General.composer, General.exploratory, General.foreign_languages,
                     General.bpm, General.freq_classical, General.freq_country,
                     General.freq_edm, General.freq_folk, General.freq_gospel, General.freq_hiphop,
                     General.freq_jazz, General.freq_kpop, General.freq_latin, General.freq_lofi,
                     General.freq_metal, General.freq_pop, General.freq_rnB, General.freq_rap, General.freq_rock,
                     General.freq_video_game_music, General.anxiety, General.depression,
                     General.insomnia, General.OCD, General.music_effect)
SELECT (SELECT Streaming.streaming_id
        FROM Streaming
        WHERE Streaming.streaming_name = Listen.Service),
       (SELECT Genre.genre_id
        FROM Genre
        WHERE Genre.genre_name = Listen.FavGenre),
       Listen.Age,
       Listen.HoursPerDay,
       Listen.WhileWorking,
       Listen.Instrumentalist,
       Listen.Composer,
       Listen.Exploratory,
       Listen.ForeignLanguages,
       Listen.BPM,
       Listen.FreqClassical,
       Listen.FreqCountry,
       Listen.FreqEdm,
       Listen.FreqFolk,
       Listen.FreqGospel,
       Listen.FreqHipHop,
       Listen.FreqJazz,
       Listen.FreqKpop,
       Listen.FreqLatin,
       Listen.FreqLofi,
       Listen.FreqMetal,
       Listen.FreqPop,
       Listen.FreqRnB,
       Listen.FreqRap,
       Listen.FreqRock,
       Listen.FreqVideoGameMusic,
       Listen.Anxiety,
       Listen.Depression,
       Listen.Insomnia,
       Listen.OCD,
       Listen.MusicEffect
FROM Listen;

UPDATE General
    SET General.streaming_id = 6
    WHERE General.streaming_id IS NULL;
/*Listen*/

select * from General
inner join Streaming USING (streaming_id)
inner join Genre USING (genre_id);


/* Какой в среднем возраст использует какой сервис [done]*/
SELECT
    ROUND(AVG(Age)) AS 'Average Age',
    streaming_name  'Service'
FROM General
INNER JOIN Streaming USING (streaming_id)
GROUP BY streaming_name;

/* Сколько людей слушают музыку и какую, когда работают? [done]*/
SELECT genre_name,
       count(genre_name)
FROM General
         INNER JOIN Genre USING (genre_id)
WHERE while_working = 'Yes'
GROUP BY genre_name
ORDER BY count(genre_name) DESC;


/* Какие жанры и сколько людей слушают их после 50?*/
SELECT genre_name AS 'Жанр',
       COUNT(age) AS 'Количество слушателей'
FROM General
         INNER JOIN Genre USING (genre_id)
WHERE age > 50
GROUP BY genre_name
ORDER BY COUNT(age) DESC;

/* Какие жанры помогают при бессоннице?*/
SELECT genre_name                AS 'Жанр',
       ROUND(AVG(hours_per_day)) AS 'Сколько часов в день',
       COUNT(genre_name)         AS 'Слушатели, которым помогло'
FROM General
         INNER JOIN Genre USING (genre_id)
         INNER JOIN Streaming USING (streaming_id)
WHERE insomnia >= 7
  AND music_effect = 'Improve'
GROUP BY genre_name;

/* В каком году стартанул сервис и сколько в нем пользователей?*/
SELECT streaming_name AS 'Стриминг',
       launch AS 'Год основания',
       active_users_mlns AS 'Активных пользователей, млн'
FROM Streaming
WHERE streaming_name NOT LIKE 'I do%'
  AND streaming_name NOT LIKE 'Oth%'
ORDER BY active_users_mlns DESC;

/* Какие жанры помогают при депрессии?*/
SELECT genre_name                AS 'Жанр',
       ROUND(AVG(hours_per_day)) AS 'Сколько часов в день',
       COUNT(genre_name)         AS 'Слушатели, которым помогло'
FROM General
         INNER JOIN Genre USING (genre_id)
         INNER JOIN Streaming USING (streaming_id)
WHERE depression >= 7
  AND music_effect = 'Improve'
GROUP BY genre_name
order by COUNT(genre_name) DESC;




