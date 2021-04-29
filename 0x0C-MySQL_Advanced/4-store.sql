-- Task 3
-- List all bands with Glam rock as their main style, ranked by their longevity
CREATE TRIGGER before_order_update BEFORE INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
