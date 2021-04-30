-- Task 7
-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections cor WHERE cor.user_id = user_id)
    WHERE id = user_id;
END$$
DELIMITER ;
