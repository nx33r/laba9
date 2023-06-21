public class Camera {
    private String model;
    private String resolution;
    private double zoom;
    private String memoryCardType;
    private int photosCount;

    public Camera(String model, String resolution, double zoom, String memoryCardType, int photosCount) {
        this.model = model;
        this.resolution = resolution;
        this.zoom = zoom;
        this.memoryCardType = memoryCardType;
        this.photosCount = photosCount;
    }

    public void resetZoom() {
        this.zoom = 1;
    }

    public void savePhoto() {
        this.photosCount++;
    }

    public void eraseMemory() {
        this.photosCount = 0;
    }

    public void changeSettings(String resolution, double zoom) {
        this.resolution = resolution;
        this.zoom = zoom;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    public double getZoom() {
        return zoom;
    }

    public void setZoom(double zoom) {
        this.zoom = zoom;
    }

    public String getMemoryCardType() {
        return memoryCardType;
    }

    public void setMemoryCardType(String memoryCardType) {
        this.memoryCardType = memoryCardType;
    }

    public int getPhotosCount() {
        return photosCount;
    }

    public void setPhotosCount(int photosCount) {
        this.photosCount = photosCount;
    }

    public static void main(String[] args) {

        Camera camera = new Camera("Canon", "1024x768", 1.0, "SD", 0);
        System.out.println("Model: " + camera.getModel());
        System.out.println("Resolution: " + camera.getResolution());
        System.out.println("Zoom: " + camera.getZoom());
        System.out.println("Memory Card Type: " + camera.getMemoryCardType());
        System.out.println("Photos Count: " + camera.getPhotosCount());

        camera.savePhoto();
        System.out.println("Photos Count after saving a photo: " + camera.getPhotosCount());

        camera.resetZoom();
        System.out.println("Zoom after resetting: " + camera.getZoom());

        camera.eraseMemory();
        System.out.println("Photos Count after erasing memory: " + camera.getPhotosCount());

        camera.changeSettings("2048x1536", 2.0);
        System.out.println("Resolution after changing settings: " + camera.getResolution());
        System.out.println("Zoom after changing settings: " + camera.getZoom());
    }
}
