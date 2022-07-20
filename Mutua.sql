CREATE TABLE `marks` (
  `mark_id` int PRIMARY KEY,
  `stdn_id` int,
  `subject_id` int,
  `day` text,
  `mark` int
);

CREATE TABLE `students` (
  `student_id` int PRIMARY KEY,
  `student_name` text,
  `group_id` int
);

CREATE TABLE `groups` (
  `group_id` int PRIMARY KEY,
  `name` text
);

CREATE TABLE `subjects` (
  `subject_id` int PRIMARY KEY,
  `title` text
);

CREATE TABLE `teachers` (
  `teacher_id` int PRIMARY KEY,
  `first_name` text,
  `last_name` text
);

CREATE TABLE `relating` (
  `subject_id` int,
  `teachers_id` int,
  `group_id` int,
  `mark_id` int,
  `student_id` int
);

ALTER TABLE `relating` ADD FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`subject_id`);

ALTER TABLE `relating` ADD FOREIGN KEY (`teachers_id`) REFERENCES `teachers` (`teacher_id`);

ALTER TABLE `relating` ADD FOREIGN KEY (`group_id`) REFERENCES `groups` (`group_id`);

ALTER TABLE `relating` ADD FOREIGN KEY (`mark_id`) REFERENCES `marks` (`mark_id`);

ALTER TABLE `relating` ADD FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);
