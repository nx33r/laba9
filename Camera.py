class CameraManager:
    def __init__(self):
        self.cameras = []

    def __len__(self):
        return len(self.cameras)

    def __getitem__(self, index):
        return self.cameras[index]

    def __iter__(self):
        return iter(self.cameras)

    def do_something_for_all(self, abstract_class_method):
        results = [abstract_class_method(camera) for camera in self.cameras]
        return results

    def get_camera_with_index(self):
        return [(i, camera) for i, camera in enumerate(self.cameras)]

    def get_camera_with_result(self, abstract_class_method):
        results = self.do_something_for_all(abstract_class_method)
        return zip(self.cameras, results)

    def get_attributes_by_type(self, data_type):
        attributes = {key: value for camera in self.cameras for key, value in camera.__dict__.items()
                      if isinstance(value, data_type)}
        return attributes

    def check_conditions(self, condition):
        all_condition = all(condition(camera) for camera in self.cameras)
        any_condition = any(condition(camera) for camera in self.cameras)
        return {"all": all_condition, "any": any_condition}

    def main(self):
        digital_camera = Camera("Canon", "D200", "50mm")
        digital_camera.resolution = "1024x768"
        digital_camera.zoom = 1.0
        digital_camera.memory_card_type = "SD"
        digital_camera.photos_count = 0
        self.cameras.append(digital_camera)

        film_camera = Camera("Nikon", "F3", "35mm")
        film_camera.film_type = "35mm"
        film_camera.film_iso = 400
        self.cameras.append(film_camera)

        for camera in self.cameras:
            print(camera.take_photo())


class Camera:
    def __init__(self, brand, model, lens):
        self.brand = brand
        self.model = model
        self.lens = lens

    def take_photo(self):
        pass

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_lens(self):
        return self.lens

    def set_lens(self, lens):
        self.lens = lens


class DigitalCamera(Camera):
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type, photos_count):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count

    def take_photo(self):
        return f"Digital Camera Photo: Resolution - {self.resolution}, Zoom - {self.zoom}"

    def save_photo(self):
        self.photos_count += 1

    def erase_memory(self):
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        self.resolution = resolution
        self.zoom = zoom

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, resolution):
        self.resolution = resolution

    def get_zoom(self):
        return self.zoom

    def set_zoom(self, zoom):
        self.zoom = zoom

    def get_memory_card_type(self):
        return self.memory_card_type

    def set_memory_card_type(self, memory_card_type):
        self.memory_card_type = memory_card_type

    def get_photos_count(self):
        return self.photos_count

    def set_photos_count(self, photos_count):
        self.photos_count = photos_count


class FilmCamera(Camera):
    def __init__(self, brand, model, lens, film_type, film_iso):
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso

    def take_photo(self):
        return f"Film Camera Photo: Film Type - {self.film_type}, Film ISO - {self.film_iso}"

    def get_film_type(self):
        return self.film_type

    def set_film_type(self, film_type):
        self.film_type = film_type

    def get_film_iso(self):
        return self.film_iso

    def set_film_iso(self, film_iso):
        self.film_iso = film_iso


if __name__ == "__main__":
    manager = CameraManager()
    manager.main()
