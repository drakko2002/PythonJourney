from app.pc_application import PCApplication

if __name__ == "__main__":
    app = PCApplication(queue_size=3, num_producers=2, num_consumers=2, runtime=10)
    app.run()