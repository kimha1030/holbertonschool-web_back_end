-- Task 13
-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users u
    SET average_score = (SELECT (SUM(score * weight)) / SUM(weight)
    FROM corrections c
    INNER JOIN projects s ON (s.id = c.project_id)
    WHERE u.id = c.user_id);
END$$
DELIMITER ;
