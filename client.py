from urllib import response
import grpc
import emailService_pb2 as pb2
import emailService_pb2_grpc as pb2_grpc

def slice_email(i_email):
    with grpc.insecure_channel('localhost:50051')as channel:
        stub = pb2_grpc.EmailhandlerStub(channel)
        response = stub.Email(pb2.email_request(emailAddress=i_email))
        return {'username':response.username,'domain':response.domain}

def client():
    while True:
        email= input("email address?\n")
        o_email = slice_email(email)
        print(o_email)


if __name__ == '__main__':
    client()