-- Task 12
-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id int)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT (SUM(score * weight)) / SUM(weight) 
    FROM corrections c 
    INNER JOIN projects s ON (s.id = c.project_id) 
    WHERE c.user_id = user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END$$
DELIMITER ;
