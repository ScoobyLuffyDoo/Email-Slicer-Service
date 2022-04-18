from concurrent import futures

import grpc
import emailService_pb2 as pb2
import emailService_pb2_grpc as pb2_grpc
import resources

class Emailhandler(pb2_grpc.EmailhandlerServicer):
    def Email(self, request,context):
        inputEmail = request.emailAddress
        print(inputEmail)     
        is_email = resources.EmailSlicer.checkEmailAddress(inputEmail)
        if is_email:
            email_service= resources.EmailSlicer()
            email_response =email_service.sliceEmail(inputEmail)
            o_username =email_response['username']
            o_domain = email_response['domain']
        else:
            pass
        return pb2.sliced_email(username=o_username,domain=o_domain)


def server():
    print("Starting Server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_EmailhandlerServicer_to_server(Emailhandler(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server is running on port :50051')
    server.wait_for_termination()

if __name__ == '__main__':
    server()
