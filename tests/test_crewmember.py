from app.models.crewmember import CrewMember

def test_upgrade_attribute():
    bob = CrewMember("Bob", "human/male")
    
    # Not eligible to upgrade
    # Picked a nonexistent attribute
    # Picked an attribute whose value is already full
    bob.status['upgrades_ready'] = 0
    ineligible = bob.upgrade_attribute("tactical")

    bob.status['upgrades_ready'] = 1
    nonexistent = bob.upgrade_attribute("finger foods")

    bob.attributes['tactical'] = 10
    bob.status['upgrades_ready'] = 1
    fullstat = bob.upgrade_attribute("tactical")

    bob.status['upgrades_ready'] = 1
    bob.attributes['tactical'] = 1
    happy_path = bob.upgrade_attribute("tactical")

    assert ineligible == False
    assert nonexistent == False
    assert fullstat == False

    assert happy_path == True

def test_get_attribute():
    bob = CrewMember("Bob", "human/male")

    bobs_engineering = bob.get_attribute("engineering")
    bobs_engineering_misspelled = bob.get_attribute("enjineering")

    assert bobs_engineering > 0
    assert bobs_engineering_misspelled == -1

def test_add_xp():
    bob = CrewMember("Bob", "human/male")

    assert bob.status['experience'] == 0
    assert bob.status['upgrades_ready'] == 0

    bob.add_xp(50)

    assert bob.status['experience'] == 50
    assert bob.status['upgrades_ready'] == 0

    bob.add_xp(100)
    
    assert bob.status['experience'] == 50
    assert bob.status['upgrades_ready'] == 1

def test_bobs_health():
    bob = CrewMember("Bob", "human/male")

    assert bob.status['health'] == 100
    assert bob.status['image_file'] == 'normal'

    bob.damage_health(15)

    assert bob.status['health'] == 85
    assert bob.status['image_file'] == 'wounded'

    bob.restore_health(10)

    assert bob.status['health'] == 95
    assert bob.status['image_file'] == 'wounded'

    bob.restore_health(6)

    assert bob.status['health'] == 100
    assert bob.status['image_file'] == 'normal'
    
    bob.damage_health(100)

    assert bob.status['health'] == 0
    assert bob.status['status'] == 'Dead'
    assert bob.status['image_file'] == 'dead'

    bob.restore_health(10)
    
    assert bob.status['health'] == 0
    assert bob.status['status'] == 'Dead'
    assert bob.status['image_file'] == 'dead'
    