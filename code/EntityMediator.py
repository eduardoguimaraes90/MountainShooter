from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:


    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(ent: Entity):
        for entity in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)